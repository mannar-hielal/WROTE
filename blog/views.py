from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'list.html'


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
    return render(request,
                  'detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})


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
