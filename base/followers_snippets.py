def run_js_script(username):
    script = f"""
    const username = "{username}";

    let followers = [];
    let followings = [];
    let dontFollowMeBack = [];
    let iDontFollowBack = [];

    (async () => {{
      try {{
        console.log(`Process started! Give it a couple of seconds`);

        const userQueryRes = await fetch(
          `https://www.instagram.com/web/search/topsearch/?query=${{username}}`
        );

        const userQueryJson = await userQueryRes.json();

        const userId = userQueryJson.users.map(u => u.user)
                                          .filter(
                                            u => u.username === username
                                           )[0].pk;

        let after = null;
        let has_next = true;

        while (has_next) {{
          await fetch(
            `https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables=` +
              encodeURIComponent(
                JSON.stringify({{
                  id: userId,
                  include_reel: true,
                  fetch_mutual: true,
                  first: 50,
                  after: after,
                }})
              )
          )
            .then((res) => res.json())
            .then((res) => {{
              has_next = res.data.user.edge_followed_by.page_info.has_next_page;
              after = res.data.user.edge_followed_by.page_info.end_cursor;
              followers = followers.concat(
                res.data.user.edge_followed_by.edges.map(({{ node }}) => {{
                  return {{
                    username: node.username,
                    full_name: node.full_name,
                  }};
                }})
              );
            }});
        }}
        console.log({{ followers }});
        return {{followers}};

        console.log(
          `Process is done: Type 'copy(followers)' or 'copy(followings)' or 'copy(dontFollowMeBack)' or 'copy(iDontFollowBack)' in the console and paste it into a text editor to take a look at it'`
        );
      }} catch (err) {{
        console.log({{ err }});
      }}
    }})();
    """
    return script


def get_followers():
    pass
