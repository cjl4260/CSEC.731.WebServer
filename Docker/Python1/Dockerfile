FROM python:3.9

WORKDIR /app

# Copy the rest of the application files
COPY Code /app/


# Expose the port that the application runs on
EXPOSE 4000

# Run the command to start the application
CMD ["python", "Server.py", "0.0.0.0" , "4000"]
