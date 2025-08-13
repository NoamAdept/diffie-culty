
# diffie-culty

A collection of Capture-the-Flag challenges exploring weaknesses in the Diffie–Hellman Key Exchange (DHKE) algorithm.

Each level demonstrates a specific flaw or weak parameter choice, ranging from toy examples you can brute-force to more realistic attacks requiring specialized algorithms.


# The Discrete Log Problem

https://sdmntpritalynorth.oaiusercontent.com/files/00000000-949c-6246-ba6e-f95d26b6e461/raw?se=2025-08-13T09%3A56%3A19Z&sp=r&sv=2024-08-04&sr=b&scid=fee8efe5-9d41-5379-a318-a3d0ee8a8820&skoid=82a3371f-2f6c-4f81-8a78-2701b362559b&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-08-13T05%3A48%3A51Z&ske=2025-08-14T05%3A48%3A51Z&sks=b&skv=2024-08-04&sig=GNoMFKGFdCJb7/VJjK4cP3FbGTV2qO5gVYBKq4AGDek%3D<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/b91a6ae5-bc35-49c1-8abf-d7ae47ae7f10" />


---

## Levels

- **Level 1 – Tiny Prime**  
  Parameters are so small you can brute-force the private key in seconds.  
  Goal: Learn the basics of the discrete logarithm problem.

- **Level 2 – Weak but Not Tiny**  
  Medium-sized prime that can’t be brute-forced directly but can be solved with baby-step giant-step or Pollard’s rho.

- **(Planned) Level 3 – Small Subgroup Trap**  
  Exploit DHKE when the generator doesn’t produce the full multiplicative group.

- **(Planned) Level 4 – Realistic p but Leaky Implementation**  
  Learn about side-channels and timing attacks.

---

## General Challenge Structure

For every level:

1. **Server** generates a private key `a` and computes `A = g^a mod p`.
2. It sends `(p, g, A)` to the player.
3. The player computes `a` using the intended exploit for that level.
4. On correct submission, the server reveals a one-time flag stored in `/flag.txt` and deletes it.

---

## Running a Challenge

Each level is packaged as a Docker container:

```bash
docker build -t diffie-culty-levelX .
docker run --rm -p 31337:31337 diffie-culty-levelX
````

Connect with:

```bash
nc localhost 31337
```

---

## Example Interaction (Level 1)

```
Welcome to DHKE Level 1!
p = 23
g = 5
A = 8
Send your answer as: a=<integer>
>
```

Goal: Find `a` such that `g^a mod p == A`.

---

## Educational Goals

* Understand the discrete logarithm problem.
* See how small primes make DHKE trivial to break.
* Learn efficient algorithms for solving discrete logs.
* Recognize bad parameter choices and insecure generators.

---

## Repository Structure

* `level1/` — tiny prime brute-force challenge.
* `level2/` — medium prime, requires baby-step giant-step or Pollard’s rho.
* `common/` — shared utility code for generating flags and handling TCP connections.

---
