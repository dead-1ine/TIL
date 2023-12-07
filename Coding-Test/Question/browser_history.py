class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:
    def __init__(self, homepage):
        self.head = self.current = ListNode(val=homepage)

    def visit(self, url):
        self.current.next = ListNode(val=url, prev=self.current)
        self.current = self.current.next
        return None

    def back(self, steps):
        while steps > 0 and self.current.prev is not None:
            steps -= 1
            self.current = self.current.prev
        return self.current.val

    def forward(self, steps):
        while steps > 0 and self.current.next is not None:
            steps -= 1
            self.current = self.current.next
        return self.current.val


# Test
browser_history = BrowserHistory('leetcode.com')

browser_history.visit('google.com')
browser_history.visit('facebook.com')
browser_history.visit('youtube.com')

browser_history.back(1)
browser_history.back(1)

browser_history.forward(1)

browser_history.visit('youtube.com')

browser_history.forward(2)

browser_history.back(2)
browser_history.back(7)