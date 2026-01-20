import os

tasks = [
    ("Hello World Page", "01_hello_world.html", "<h1>Hello World!</h1><p>Welcome to my first HTML page.</p>"),
    ("Simple Resume Page", "02_resume.html", "<h1>John Doe</h1><p>Software Engineer</p><h2>Experience</h2><ul><li>Company A - Dev</li><li>Company B - Intern</li></ul>"),
    ("Favorite Books or Movies List", "03_favorites.html", "<h1>My Favorites</h1><h2>Movies</h2><ul><li>Inception</li><li>The Matrix</li></ul><h2>Books</h2><ul><li>1984</li><li>The Great Gatsby</li></ul>"),
    ("Basic Contact Info Page", "04_contact.html", "<h1>Contact Me</h1><p>Email: john@example.com</p><p>Phone: 123-456-7890</p>"),
    ("HTML Table with Student Grades", "05_grades.html", "<h1>Student Grades</h1><table border='1'><tr><th>Student</th><th>Grade</th></tr><tr><td>Alice</td><td>A</td></tr><tr><td>Bob</td><td>B</td></tr></table>"),
    ("Simple Blog Post Page", "06_blog_post.html", "<h1>My First Blog Post</h1><p>Published on: Oct 1, 2023</p><p>This is the content of my blog post. It is very interesting.</p>"),
    ("Product Landing Page", "07_product_landing.html", "<h1>Super Widget</h1><p>The best widget in the world. Buy now!</p><button>Buy Now</button>"),
    ("Tribute Page", "08_tribute.html", "<h1>Tribute to Ada Lovelace</h1><p>The first computer programmer.</p><img src='https://upload.wikimedia.org/wikipedia/commons/a/a4/Ada_Lovelace_portrait.jpg' alt='Ada Lovelace' width='200'>"),
    ("Photo Gallery Page", "09_gallery.html", "<h1>My Photo Gallery</h1><div style='display:flex;'><div style='margin:10px; border:1px solid #ccc; padding:5px;'>Photo 1</div><div style='margin:10px; border:1px solid #ccc; padding:5px;'>Photo 2</div></div>"),
    ("Personal Portfolio Page", "10_portfolio.html", "<h1>My Portfolio</h1><p>Check out my projects below.</p><ul><li>Project 1</li><li>Project 2</li></ul>"),
    ("Survey or Feedback Form", "11_survey.html", "<h1>Feedback Form</h1><form><label>Name:</label><input type='text'><br><label>Comments:</label><textarea></textarea><br><input type='submit'></form>"),
    ("Newsletter Signup Form", "12_newsletter.html", "<h1>Newsletter Signup</h1><form><label>Email:</label><input type='email'><button>Subscribe</button></form>"),
    ("Simple Event Invitation Page", "13_event_invitation.html", "<h1>Birthday Party!</h1><p>You are invited to my party on Friday.</p><p>Location: My House</p>"),
    ("Recipe Page", "14_recipe.html", "<h1>Pancake Recipe</h1><h2>Ingredients</h2><ul><li>Flour</li><li>Milk</li><li>Eggs</li></ul><h2>Steps</h2><ol><li>Mix</li><li>Fry</li></ol>"),
    ("Event Schedule Page", "15_schedule.html", "<h1>Conference Schedule</h1><table border='1'><tr><th>Time</th><th>Event</th></tr><tr><td>9:00 AM</td><td>Keynote</td></tr><tr><td>10:00 AM</td><td>Workshop</td></tr></table>"),
    ("Simple Login Page (Front-End Only)", "16_login.html", "<h1>Login</h1><form><label>Username:</label><input type='text'><br><label>Password:</label><input type='password'><br><button>Login</button></form>"),
    ("Basic Registration Form", "17_registration.html", "<h1>Register</h1><form><label>Name:</label><input type='text'><br><label>Email:</label><input type='email'><br><label>Password:</label><input type='password'><br><button>Register</button></form>"),
    ("HTML Page with Embedded YouTube Video", "18_youtube.html", "<h1>Watch this video</h1><iframe width='560' height='315' src='https://www.youtube.com/embed/dQw4w9WgXcQ' frameborder='0' allowfullscreen></iframe>"),
    ("Coming Soon Landing Page", "19_coming_soon.html", "<h1>Coming Soon</h1><p>We are working hard to launch our new site. Stay tuned!</p>"),
    ("HTML FAQ Page", "20_faq.html", "<h1>Frequently Asked Questions</h1><h3>Q: What is this?</h3><p>A: This is a collection of HTML pages.</p><h3>Q: How do I use it?</h3><p>A: Just open the files.</p>"),
    ("Basic HTML Page with Audio Player", "21_audio_player.html", "<h1>Audio Player</h1><audio controls><source src='horse.ogg' type='audio/ogg'>Your browser does not support the audio element.</audio>"),
    ("Simple HTML Page with Google Maps Embed", "22_google_maps.html", "<h1>Our Location</h1><iframe src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3151.8354345093647!2d144.9537353153166!3d-37.816279742021234!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6ad642af0f11fd81%3A0xf577d1b74b1d8e1c!2sFederation%20Square!5e0!3m2!1sen!2sau!4v1614131580000!5m2!1sen!2sau' width='600' height='450' style='border:0;' allowfullscreen='' loading='lazy'></iframe>"),
    ("404 Error Page", "23_404.html", "<h1>404 - Not Found</h1><p>Sorry, the page you are looking for does not exist.</p><a href='01_hello_world.html'>Go Home</a>"),
    ("HTML Page with Table of Contents", "24_toc.html", "<h1>Table of Contents</h1><ul><li><a href='#sec1'>Section 1</a></li><li><a href='#sec2'>Section 2</a></li></ul><h2 id='sec1'>Section 1</h2><p>Content of section 1.</p><h2 id='sec2'>Section 2</h2><p>Content of section 2.</p>"),
    ("Simple Image Slider (Manual HTML Version)", "25_slider.html", "<h1>Image Slider</h1><div style='width:300px; height:200px; overflow:hidden; border:1px solid black;'><div style='width:900px; display:flex;'><div style='width:300px;'>Slide 1</div><div style='width:300px;'>Slide 2</div><div style='width:300px;'>Slide 3</div></div></div><p>Manual slider (scroll horizontally or imagine buttons here).</p>")
]

os.makedirs("html_pages", exist_ok=True)

for title, filename, content in tasks:
    with open(os.path.join("html_pages", filename), "w") as f:
        f.write(f"<!DOCTYPE html><html><head><title>{title}</title></head><body>{content}</body></html>")

print("Generated 25 HTML files.")
