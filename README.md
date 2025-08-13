# DHKE CTF — Level 1 (pwn.college style)

A tiny service that simulates an insecure Diffie–Hellman exchange.
Your goal: **recover Alice's private exponent `a`** from `p`, `g`, and `A = g^a mod p`,
then submit `a` to the service to receive the flag.

- The service generates a **random flag** at container start and saves it to `/flag.txt`.
- The flag file is **only revealed after you solve the challenge**. On success, the server
  prints the flag and **deletes `/flag.txt`** so it cannot be read again.
- Parameters are intentionally tiny (Level 1): brute forcing the discrete log is enough.

## Run (Docker)

```bash
docker build -t dhke-level1 .
docker run --rm -p 31337:31337 dhke-level1
# In another terminal:
nc localhost 31337
```

## Interaction

On connect, you'll see something like:
```
Welcome to DHKE Level 1!
p = 23
g = 5
A = 8
Send your answer as: a=<integer>
> 
```

You must compute `a` such that `g^a mod p == A` and send `a=<integer>`.
If correct, you get the flag. Otherwise you are disconnected.

## Tips

- For Level 1, just brute force `a` in `[2, p-2]` until `pow(g, a, p) == A`.
- This is teaching you what the discrete logarithm problem is in the smallest toy setting.

## Files

- `server.py` — challenge service.
- `Dockerfile` — container for deployment.
- `run.sh` — entrypoint script (creates one-time flag).
- `solve_example.py` — a reference solver (do not ship to players).
