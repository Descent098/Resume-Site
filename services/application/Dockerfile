FROM python:latest

# Copy necessary app files
ADD static /site/static
COPY requirements.txt /site
COPY routes.py /site


# Switch to folder with all code in it
WORKDIR /site

# Install Dependencies
RUN pip install -r requirements.txt

# Run Flask Project
CMD ["python", "routes.py"]