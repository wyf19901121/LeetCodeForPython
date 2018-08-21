class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) == 0 and len(p) == 0:
            return True
        if len(p) == 0:
            return False
        if len(s) == 0 and len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:])
        if len(s) == 0:
            return False

        if s[0] == p[0] or p[0] == '.':
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                return self.isMatch(s[1:], p[1:])
        else:
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s, p[2:])
            else:
                return False
