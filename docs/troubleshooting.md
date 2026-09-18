## Resolving issues

Network issue:
1. go to chrome://net-internals/#sockets, and click Flush socket pools.
2. go to chrome://net-internals/#dns, and click Clear host cache.
3. go to chrome://net-internals/#hsts, navigate to Delete domain security policies, and enter nanogchen.github.io, click Delete.
4. open terminal and run: ipconfig /flushdns
