**Author:** Matthew Holder
**Version:** 0.1

[PR]()

Problem Domain:

Build a project with one model and one app using django views.

Description:

Admin:
- Admin page has creation/modification/deletion access to list of Snacks with name/purchaser/description info.
- Admin page has second user asside from super user.

Base:
- Base.html (aka the home page) uses snack_list.html to list Snacks.
- Each snack can be clicked on to render a new page using the primary key to load details about the snack clicked on.

Testing:
- Testing checks for a 200 status code and proper template use.
- Testing also carries a description of why we are unable to easily test the details page with what we've learned so far.