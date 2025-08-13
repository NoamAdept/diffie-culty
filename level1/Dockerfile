# Minimal Python image
FROM python:3.11-alpine

# Create app directory
WORKDIR /app

# Copy files
COPY server.py /app/server.py
COPY run.sh /app/run.sh

# Expose service port
EXPOSE 31337

# Make run.sh executable
RUN chmod +x /app/run.sh

# Create an unprivileged user
RUN adduser -D ctf && chown -R ctf:ctf /app
USER ctf

# Entrypoint
ENTRYPOINT ["/app/run.sh"]
