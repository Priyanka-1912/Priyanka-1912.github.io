# Priyanka's Portfolio & Blog

This is the source code for my personal portfolio and blog, hosted on GitHub Pages.

## Tech Stack
- **Frontend:** HTML5, CSS3 (Vanilla)
- **Blog Engine:** Python (custom script using the `markdown` library)
- **Hosting:** GitHub Pages

## How to use this repository

### 1. Initial Setup
If you are setting this up for the first time:
1. Install the required Python library:
   ```bash
   pip install markdown
   ```

### 2. Writing a New Blog Post
1. Go to the `src/content/` folder.
2. Create a new file ending in `.md` (e.g., `my-new-post.md`).
3. Add the following header at the top of your file:
   ```markdown
   ---
   title: Your Post Title
   date: May 5, 2026
   ---
   Your blog content goes here...
   ```

### 3. Building the Site
Every time you add or edit a blog post, run the builder script:
```bash
python src/build.py
```
This will:
- Convert your Markdown files into HTML in the `blog/` folder.
- Automatically update `blog.html` with a link to your new post.

### 4. Deploying to GitHub Pages
1. Save all your changes:
   ```bash
   git add .
   git commit -m "Add new blog post"
   ```
2. Push to GitHub:
   ```bash
   git push origin main
   ```
3. Your site will be live at `https://Priyanka-1912.github.io/`!

## Customization
- **Theme Colors:** You can change the colors in `style.css` under the `:root` section.
- **Portfolio Data:** Update `index.html` to change your experience, education, or contact details.
