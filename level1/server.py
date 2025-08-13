#!/usr/bin/env python3
import os
import socketserver
import secrets

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", "31337"))

# Level 1 toy parameters (intentionally tiny)
P = 23
G = 5

BANNER = (
    "Welcome to DHKE Level 1!\n"
    "Recover Alice's private exponent a from (p, g, A = g^a mod p).\n"
    "Submit as: a=<integer>\n\n"
).encode()

# Use a writable default; can be overridden via env
FLAG_PATH = os.environ.get("FLAG_PATH", "/home/ctf/flag.txt")


def gen_private(p: int) -> int:
    """private a in [2, p-2]"""
    return 2 + secrets.randbelow(p - 3)


class Handler(socketserver.StreamRequestHandler):
    def handle(self):
        a = gen_private(P)
        A = pow(G, a, P)

        try:
            self.wfile.write(BANNER)
            self.wfile.write(f"p = {P}\n".encode())
            self.wfile.write(f"g = {G}\n".encode())
            self.wfile.write(f"A = {A}\n".encode())
            self.wfile.write(b"Send your answer as: a=<integer>\n> ")
            self.wfile.flush()

            # read one line with a timeout
            self.request.settimeout(30.0)
            line = self.rfile.readline(256).decode(errors="ignore").strip()

            if not line.startswith("a="):
                self.wfile.write(b"\nBad format. Bye.\n")
                return

            try:
                submitted = int(line.split("=", 1)[1].strip())
            except Exception:
                self.wfile.write(b"\nNot an integer. Bye.\n")
                return

            if submitted == a:
                # Success — print and delete the one-time flag
                if os.path.exists(FLAG_PATH):
                    with open(FLAG_PATH, "r") as f:
                        flag = f.read().strip()
                    try:
                        os.remove(FLAG_PATH)
                    except Exception:
                        pass
                    self.wfile.write(b"\nCorrect!\n")
                    self.wfile.write(f"Here is your flag: {flag}\n".encode())
                else:
                    self.wfile.write(b"\nCorrect, but the flag has already been claimed.\n")
            else:
                self.wfile.write(b"\nNope. Better luck next time.\n")

        except Exception:
            # Don't leak server internals to players
            try:
                self.wfile.write(b"\nError.\n")
            except Exception:
                pass


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True


def main():
    with ThreadedTCPServer((HOST, PORT), Handler) as srv:
        print(f"[+] Listening on {HOST}:{PORT}", flush=True)
        srv.serve_forever()


if __name__ == "__main__":
    main()

