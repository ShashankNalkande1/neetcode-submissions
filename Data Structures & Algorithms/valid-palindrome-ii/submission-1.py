class Solution:

    def validPalindrome(self, s: str) -> bool:
        # yeh main function hai jo check karega ki string
        # maximum ek character delete karke palindrome ban sakti hai ya nahi

        def check(l: int, r: int) -> bool:
            # yeh helper function hai jo substring ko check karega
            # ki l aur r ke beech ka part palindrome hai ya nahi
            
            while l < r:
                # jab tak left pointer right se chota hai tab tak check karte rahenge
                
                if s[l] != s[r]:
                    # agar left aur right characters match nahi hue
                    # to palindrome nahi hai
                    return False
                
                l += 1
                # left pointer ko ek step aage badha do
                
                r -= 1
                # right pointer ko ek step peeche le aao
            
            return True
            # agar loop complete ho gaya aur mismatch nahi mila
            # to substring palindrome hai


        left = 0
        # left pointer string ke start par set kiya

        right = len(s) - 1
        # right pointer string ke last index par set kiya


        while left < right:
            # jab tak left aur right cross nahi karte tab tak loop chalega

            if s[left] != s[right]:
                # agar dono characters match nahi hue
                # matlab ek mistake hai string me
                
                return (
                    check(left + 1, right) 
                    # option 1: left character ko skip karo
                    # matlab left+1 se right tak check karo
                    
                    or
                    
                    check(left, right - 1)
                    # option 2: right character ko skip karo
                    # matlab left se right-1 tak check karo
                )

            left += 1
            # agar characters match ho gaye
            # to left pointer ko aage badhao

            right -= 1
            # aur right pointer ko peeche lao


        return True
        # agar poori string me mismatch nahi mila
        # to string already palindrome hai