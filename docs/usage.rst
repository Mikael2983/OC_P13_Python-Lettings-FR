Usage
=====

The **OC_lettings** application offers the following features:

Main Features
-------------

- **Home page**: site overview
- **Profiles**: user profile management
- **Listings**: rental property management

Useful Commands
---------------

1. Run unit tests:

   .. code-block:: bash

      pytest

2. Build documentation:

   .. code-block:: bash

      sphinx-build -b html docs/ docs/_build/html

3. Start the local server:

   .. code-block:: bash

      python manage.py runserver

Deployment
----------

Two deployment options are available:

1. **Local deployment** (Render or classic server)
   Make sure all necessary environment variables (e.g., `SECRET_KEY`, `DEBUG`) are set.

2. **DockerHub deployment**
   A ready-to-use Docker image is available:
   `mikael2983/python_lettings_fr:latest`

   Run the container locally:

   .. code-block:: bash

      docker pull mikael2983/python_lettings_fr:latest
      docker run -d -p 8000:8000 --name oc_lettings mikael2983/python_lettings_fr:latest

   Access the application at:
   http://127.0.0.1:8000/