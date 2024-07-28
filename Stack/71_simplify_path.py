class Solution:
    def simplify_path(self, path):
        """
        :type path: str
        :rtype: str
        """
        result = []
        plist = path.split('/')
        for pos in plist:
            if pos:
                if pos == '..':
                    if result:
                        result.pop()
                elif pos != '.':
                    result.append(pos)
        return '/' + '/'.join(result)

if __name__ == "__main__":
    sol_obj = Solution()
    test_cases = [
        ("/home/", "/home"),
        ("/../", "/"),
        ("/home//foo/", "/home/foo"),
        ("/a/./b/../../c/", "/c")
    ]

    for path, expected in test_cases:
        result = sol_obj.simplify_path(path)
        print(f'Input: "{path}", Output: "{result}", Expected: "{expected}"')
        assert result == expected, f"Test failed for input {path}"
