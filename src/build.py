import os
import re
import markdown

def build():
    content_dir = 'src/content'
    template_path = 'src/templates/post.html'
    output_dir = 'blog'
    blog_list_path = 'blog.html'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    posts = []

    for filename in os.listdir(content_dir):
        if filename.endswith('.md'):
            with open(os.path.join(content_dir, filename), 'r', encoding='utf-8') as f:
                content = f.read()

            # Simple metadata extraction
            meta_match = re.match(r'---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
            if meta_match:
                meta_text = meta_match.group(1)
                body_text = meta_match.group(2)
                
                title = re.search(r'title:\s*(.*)', meta_text).group(1)
                date = re.search(r'date:\s*(.*)', meta_text).group(1)
            else:
                title = filename.replace('.md', '').title()
                date = "Unknown Date"
                body_text = content

            html_content = markdown.markdown(body_text)
            
            # Create post HTML
            post_html = template.replace('{{ title }}', title)
            post_html = post_html.replace('{{ date }}', date)
            post_html = post_html.replace('{{ content }}', html_content)

            output_filename = filename.replace('.md', '.html')
            with open(os.path.join(output_dir, output_filename), 'w', encoding='utf-8') as f:
                f.write(post_html)

            posts.append({
                'title': title,
                'date': date,
                'url': f'blog/{output_filename}'
            })

    # Update blog.html listing
    with open(blog_list_path, 'r', encoding='utf-8') as f:
        blog_page = f.read()

    blog_items_html = ""
    for post in sorted(posts, key=lambda x: x['date'], reverse=True):
        blog_items_html += f"""
        <div class="card">
            <h3><a href="{post['url']}" style="text-decoration: none; color: inherit;">{post['title']}</a></h3>
            <div class="meta">{post['date']}</div>
            <a href="{post['url']}" class="btn btn-secondary">Read More</a>
        </div>
        """

    new_blog_page = re.sub(
        r'<div id="blog-list">.*?</div>',
        f'<div id="blog-list">{blog_items_html}</div>',
        blog_page,
        flags=re.DOTALL
    )

    with open(blog_list_path, 'w', encoding='utf-8') as f:
        f.write(new_blog_page)

    print(f"Successfully built {len(posts)} blog posts!")

if __name__ == "__main__":
    try:
        build()
    except ImportError:
        print("Error: The 'markdown' library is not installed.")
        print("Please run: pip install markdown")
