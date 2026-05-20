class Solution:

    def isAlienSorted(self, words, order):

        # alien alphabet ka ranking map
        rank = {}

        # Shashank har alien character ka position store kar raha hai
        for i, ch in enumerate(order):

            rank[ch] = i

        # ab adjacent words compare karo
        for i in range(len(words) - 1):

            w1 = words[i]
            w2 = words[i + 1]

            # character by character compare
            for j in range(min(len(w1), len(w2))):

                # agar mismatch mila
                if w1[j] != w2[j]:

                    # agar first word ka character
                    # alien order me bada nikla
                    # matlab wrong sorting
                    if rank[w1[j]] > rank[w2[j]]:

                        return False

                    # warna correct hai
                    break

            else:

                # yaha matlab:
                # saare characters same the

                # example:
                # "neetcode"
                # "neet"

                # bada word pehle nahi aana chahiye
                if len(w1) > len(w2):

                    return False

        return True