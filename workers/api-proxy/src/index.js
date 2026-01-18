export default {
	async fetch(request, env, ctx) {
		const url = new URL(request.url);

		// Handle OPTIONS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, {
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'GET,POST,OPTIONS',
          'Access-Control-Allow-Headers': '*',
        },
      });
    }

		if (url.pathname.startsWith('/api/')) {
			const cache = caches.default; 

			// try to return cached response first 
			let response = await cache.match(request);

			if (!response) {
				try {
				const renderUrl = `https://portfolio-ywk1.onrender.com${url.pathname}`;

				const fetched = await fetch(renderUrl, {
          headers: { 'Accept': 'application/json' },
        });

				// Clone response before caching
				response = new Response(await fetched.text(), {
					status: fetched.status,
  				statusText: fetched.statusText,
  				headers: fetched.headers
				});
				response.headers.set(
					'Cache-Control',
					'public, max-age=600'
				);

				ctx.waitUntil(cache.put(request, response.clone()));
				} catch (err) {
					return new Response(JSON.stringify({ error: err.message }), {
            status: 500,
            headers: { 'Content-Type': 'application/json' },
          });
				}
			}
			// Add CORS headers for frontend requests
      response.headers.set('Access-Control-Allow-Origin', '*');
      response.headers.set(
        'Access-Control-Allow-Methods',
        'GET, POST, OPTIONS'
      );
      response.headers.set('Access-Control-Allow-Headers', '*');

			return response;
		}
		return new Response('Not Found', { status: 404 });
	},
};
