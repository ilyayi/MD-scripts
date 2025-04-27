import fetch from "node-fetch";

let query = "table"

const fetchData = async () => {
    const response = await fetch("https://www.facebook.com/api/graphql/", {
        "headers": {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded",
            "priority": "u=1, i",
            "sec-ch-prefers-color-scheme": "dark",
            "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
            "sec-ch-ua-full-version-list": "\"Not(A:Brand\";v=\"99.0.0.0\", \"Google Chrome\";v=\"133.0.6943.142\", \"Chromium\";v=\"133.0.6943.142\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-model": "\"\"",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-ch-ua-platform-version": "\"15.3.1\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-asbd-id": "359341",
            "x-fb-friendly-name": "CometMarketplaceSearchContentPaginationQuery",
            "x-fb-lsd": "uk5p_DCLF40PBDKLDCu3_O",
            "cookie": "", //куки подставь
            "Referer": https://www.facebook.com/marketplace/112800905400271/search?query=${encodeURIComponent(query)},
            "Referrer-Policy": "strict-origin-when-cross-origin"
        },


"body":

`av=100012132856523&__aaid=0&__user=100012132856523&__a=1&__req=1w&__hs=20202.HYP%3Acomet_pkg.2.1...0&dpr=2&__ccg=EXCELLENT&__rev=1022177078&__s=qazns9%3A9cktmz%3Avjbbot&__hsi=7496691466572068945&__dyn=7xeXzWK1ixt0mUyEqxemh0noeEb8nwgUao5ebzEdE98K360CEboG0IE6u3y4o2Gwfi0LVEtwMw6ywMwto886C11wBz81s8hwGxu782lwv89kbxS1Fwc61awkovwRwlE-U2exi4UaEW2G1jwUBwJK14xm1Wxfxmu3W3y261eBx_wHwfC2-awLyESE2KwkQ0z8c86-bwHwKG4UrwFg2fwxyo6J0qo4e4UcEeE-3WVU-4FqwIK6E4-mEbUaU3ywo8&__csr=ggMgltPuyNcrky7NDsYDPq68hextFjMD6NmJjcIJaogZRlsYgBdFlWQTEJ8B_rPOlaW4EGiqAASgyA--WF4q8DYynRLcC8Aa55GV4AaQVa88iAUHy48HAQWzELDiy8jUnz99QmirG8y9kigzG8yVoKjAhUFuWy9GHhkECdAgVpknAz4cxabypoO4ouy9FfxaKFkA4poaoLwWxam2mUWjx-agG644VoaqAxq2-2mbCyoybU-2668vwFQ58e9oKq8wEg622yex24Eb89oco888UOaxu68GdBwpUtwFwUKewLxO483Pwk82mwDwaS1-U7G3avh85yh0oo3CySxU158e84q0g-ayEbE6m0Qo4Dw7hg2gwVg26Aw8bmKh2GG3S1Jw7ew7syoZ1CcVkmbwj8rgfk19woqy87C0hW0E9U1gE1roIF84O5Fo07Jh00f3-1Hwe-0ma02Gy088g6a0mV0QwdW9yVU6W04eU0E61ng72kBwoU1uvg0JW08jg5lxG58mO0LAw1Be5E1sEeo9U0dsUow2b80QC0f2w4k80XU0jdwXw5-w2vo0_60rC7E0N8w&__comet_req=15&fb_dtsg=NAcPSUTWj9HvTeC7YcHO1JKC6GVGTovOWOY_nwCmwn3Ox1s0reGwsVw%3A1%3A1674621764&jazoest=25459&lsd=uk5p_DCLF40PBDKLDCu3_O&__spin_r=1022177078&__spin_b=trunk&__spin_t=1745459499&__crn=comet.fbweb.CometMarketplaceSearchRoute&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=CometMarketplaceSearchContentPaginationQuery&variables=%7B%22count%22%3A24%2C%22cursor%22%3A%22%7B%5C%22pg%5C%22%3A0%2C%5C%22b2c%5C%22%3A%7B%5C%22br%5C%22%3A%5C%22%5C%22%2C%5C%22it%5C%22%3A0%2C%5C%22hmsr%5C%22%3Afalse%2C%5C%22tbi%5C%22%3A0%7D%2C%5C%22c2c%5C%22%3A%7B%5C%22br%5C%22%3A%5C%22AbpawxKOwM3DeImkDYWI5F-_964-j5zOOeiauF80cypOIpy7qLxa9L0fcFFcNCndyM5GNOkCkR37-3XQZIRyRSG1PYD1Wq8tAMhZ4HRv7QnxF5blW9W9HxusyBej_0wH8eiNX2q5HUIaIw--JF2p3QeasCQWnH_1y0CFn1pFmc5JIR1d3xoKOYuzm5cao-1xh97W5NbyJrsyvVoDfzpdg4q5bXz3v6PzPW7O7oRYA0BeUn9PDA5mfPiRWIeWLSWrftIQndBMqw-HsLJvXZHgsSNqj18g1IQ1EgqviUMzVe57GHEicIzDkib0wd1P2xKibQjMYsSvICSjx_tu9NvROvEk_CZdb2d8zMdEVo4sUhnEI8e9ttZEKnuXllhP6P57Ema8DUijMy-sM68ncBVb051OddeYKIYng9ZbaeOErvd8y-3T3wMZCBSJAKh4GFI1blwRJhRTsYkiz4cnO5xH1iGinAAsbXnSAagIRY5I4WJmVVTVtf7_9h5gZIhHpfSQfa6KUWU4weSdT2IE3WS60RjiBaFmIZHYBb6O_RUYLlc1REcJ_PIliD3Rm6B7QillioQ%5C%22%2C%5C%22it%5C%22%3A24%2C%5C%22rpbr%5C%22%3A%5C%22%5C%22%2C%5C%22rphr%5C%22%3Afalse%2C%5C%22rmhr%5C%22%3Afalse%7D%2C%5C%22ads%5C%22%3A%7B%5C%22items_since_last_ad%5C%22%3A24%2C%5C%22items_retrieved%5C%22%3A24%2C%5C%22ad_index%5C%22%3A0%2C%5C%22ad_slot%5C%22%3A0%2C%5C%22dynamic_gap_rule%5C%22%3A0%2C%5C%22counted_organic_items%5C%22%3A0%2C%5C%22average_organic_score%5C%22%3A0%2C%5C%22is_dynamic_gap_rule_set%5C%22%3Afalse%2C%5C%22first_organic_score%5C%22%3A0%2C%5C%22is_dynamic_initial_gap_set%5C%22%3Afalse%2C%5C%22iterated_organic_items%5C%22%3A0%2C%5C%22top_organic_score%5C%22%3A0%2C%5C%22feed_slice_number%5C%22%3A0%2C%5C%22feed_retrieved_items%5C%22%3A0%2C%5C%22ad_req_id%5C%22%3A0%2C%5C%22refresh_ts%5C%22%3A0%2C%5C%22cursor_id%5C%22%3A54934%2C%5C%22mc_id%5C%22%3A0%2C%5C%22ad_index_e2e%5C%22%3A0%2C%5C%22seen_ads%5C%22%3A%7B%5C%22ad_ids%5C%22%3A%5B%5D%2C%5C%22page_ids%5C%22%3A%5B%5D%2C%5C%22campaign_ids%5C%22%3A%5B%5D%7D%2C%5C%22has_ad_index_been_reset%5C%22%3Afalse%2C%5C%22is_reconsideration_ads_dropped%5C%22%3Afalse%7D%2C%5C%22irr%5C%22%3Atrue%2C%5C%22serp_cta%5C%22%3Afalse%2C%5C%22rui%5C%22%3A%5B%5D%2C%5C%22mpid%5C%22%3A%5B%5D%2C%5C%22ubp%5C%22%3Anull%2C%5C%22ncrnd%5C%22%3A0%2C%5C%22irsr%5C%22%3Afalse%2C%5C%22bmpr%5C%22%3A%5B%5D%2C%5C%22bmpeid%5C%22%3A%5B%5D%2C%5C%22nmbmp%5C%22%3Afalse%2C%5C%22skrr%5C%22%3Afalse%2C%5C%22ioour%5C%22%3Afalse%2C%5C%22ise%5C%22%3Afalse%7D%22%2C%22params%22%3A%7B%22bqf%22%3A%7B%22callsite%22%3A%22COMMERCE_MKTPLACE_WWW%22%2C%22query%22%3A%22${encodeURIComponent(query)}%22%7D%2C%22browse_request_params%22%3A%7B%22commerce_enable_local_pickup%22%3Atrue%2C%22commerce_enable_shipping%22%3Atrue%2C%22commerce_search_and_rp_available%22%3Atrue%2C%22commerce_search_and_rp_category_id%22%3A%5B%5D%2C%22commerce_search_and_rp_condition%22%3Anull%2C%22commerce_search_and_rp_ctime_days%22%3Anull%2C%22filter_location_latitude%22%3A33.9583273


84528%2C%22filter_location_longitude%22%3A-118.33113348074%2C%22filter_price_lower_bound%22%3A0%2C%22filter_price_upper_bound%22%3A214748364700%2C%22filter_radius_km%22%3A64%7D%2C%22custom_request_params%22%3A%7B%22browse_context%22%3Anull%2C%22contextual_filters%22%3A%5B%5D%2C%22referral_code%22%3Anull%2C%22saved_search_strid%22%3Anull%2C%22search_vertical%22%3A%22C2C%22%2C%22seo_url%22%3Anull%2C%22surface%22%3A%22SEARCH%22%2C%22virtual_contextual_filters%22%3A%5B%5D%7D%7D%2C%22scale%22%3A2%7D&server_timestamps=true&doc_id=9082812915151057`,
        "method": "POST"
    });
    const data = await response.json();
    for(const edge of data.data.marketplace_search.feed_units.edges){
        try{
            console.log(edge.node.listing.marketplace_listing_title);
        } catch (e){
            console.log(edge.node);
        }
    }
    // console.log(data);
}

fetchData();