from django.contrib.postgres.search import SearchVector
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from taggit.models import Tag

from .models import Post, Comment
from .forms import EmailPostForm, CommentForm, SearchForm


def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__name__in=[tag]).distinct()

    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'list.html',
                  {'page': page,
                   'posts': posts,
                   'tag': tag})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    # comment funtionality
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # the reply functionality
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None

            if parent_id:
                parent_queryset = Comment.objects.filter(id=parent_id)
                if parent_queryset.exists():
                    parent_obj = parent_queryset.first()
            parent = parent_obj
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.parent = parent
            new_comment.save()
    else:
        comment_form = CommentForm()
        # Similar posts
        post_tags_ids = post.tags.values_list('id', flat=True)
        similar_posts = Post.published.filter(tags__in=post_tags_ids) \
        .exclude(id=post.id)
        similar_posts = similar_posts.annotate(same_tags=Count('tags')) \
                            .order_by('-same_tags', '-publish')[:4]

    return render(request,
                  'detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form,
                   'similar_posts':similar_posts})


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post,
                             id=post_id,
                             status='published')
    sent = False
    # when POST, process the form
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url())

            subject = f"{cleaned_data['name']} recommends you read: " \
                      f"{post.title}"
            message = f"Read {post.title} at {post_url} \n \n" \
                      f"{cleaned_data['name']} \'s comments: {cleaned_data['comments']}"

            send_mail(subject, message, cleaned_data['email'], [cleaned_data['to']])
            sent = True
    else:
        # when GET, display an empty form
        form = EmailPostForm()
    return render(request, 'share.html', {'post': post,
                                          'form': form,
                                          'sent': sent})

def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.published.annotate(
            search=SearchVector('title', 'body'),
            ).filter(search=query)
    return render(request,
        'search.html',
        {'form': form,
        'query': query,
        'results': results})