# Use an official nginx image to serve the static site
FROM nginx:alpine

# Copy the static files into the nginx html directory
COPY . /usr/share/nginx/html

# Expose the default nginx port
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
