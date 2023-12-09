class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        # parse responses; features turn into counter (idx - cnt)
        # for splitted response, check if any features mentioned
        # yes then cnt+1
        feature_cnt = {}
        for f in features:
            feature_cnt[f] = 0
        res = []
        for response in responses:
            r = response.split(' ')
            # print(r)
            
            for word in set(r):
                if word in feature_cnt:
                    feature_cnt[word] += 1

        keys = list(feature_cnt.keys())
        # print(feature_cnt)
        res = sorted(keys, key=lambda x: (-feature_cnt[x], features.index(x)))
        return res