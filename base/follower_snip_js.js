const username = "{username}";

let followers = [];

(async () => {
    try {
        console.log("Process started! Give it a couple of seconds");

        const userQueryRes = await fetch(
            `https://www.instagram.com/web/search/topsearch/?query=${username}`
        );

        const userQueryJson = await userQueryRes.json();

        const userId = userQueryJson.users
            .map(u => u.user)
            .filter(u => u.username === username)[0].pk;

        let after = null;
        let has_next = true;

        while (has_next) {
            const res = await fetch(
                `https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables=` +
                encodeURIComponent(
                    JSON.stringify({
                        id: userId,
                        include_reel: true,
                        fetch_mutual: true,
                        first: 50,
                        after: after,
                    })
                )
            );
            const data = await res.json();
            has_next = data.data.user.edge_followed_by.page_info.has_next_page;
            after = data.data.user.edge_followed_by.page_info.end_cursor;
            followers = followers.concat(
                data.data.user.edge_followed_by.edges.map(({ node }) => {
                    return {
                        username: node.username,
                        full_name: node.full_name,
                    };
                })
            );
        }
        console.log({ followers });
        // Pass followers back to Python
        return { followers };
    } catch (err) {
        console.error(err);
        // Pass error back to Python
        throw err;
    }
})();
