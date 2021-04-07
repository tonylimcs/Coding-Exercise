"""
Rearrange a given singly linked list such as below:
Input: l1 -> l2 -> l3 -> ... -> ln-1 -> ln
Expected: l1 -> ln -> l2 -> ln-1 -> l3 -> ...

Example:
Input: 1-2-3-4-5-6-7-8
Output: 1-8-2-7-3-6-4-6-5
"""


class Link:
    def __init__(self, value):
        self.value = value
        self.nex = None


def parse(ls_):
    head = Link(ls_[0])
    cur_ = head
    for i in range(1, len(ls_)):
        cur_.nex = Link(ls_[i])
        cur_ = cur_.nex   # Update
    return head


def traverse(ll_, n_):
    cur_ = ll_
    for i in range(0, n_):
        cur_ = cur_.nex
    return cur_


def rearrange(ll_, n):
    mid = len(ls) // 2 + len(ls) % 2

    cur_ = ll_
    for i in range(0, mid):
        # Get edge link
        nex = traverse(cur_, n - 1)

        # Update linked list
        tmp = cur_.nex
        cur_.nex = nex
        cur_.nex.nex = tmp

        # Update current pointer
        cur_ = cur_.nex.nex
        n -= 2
    cur_.nex = None  # Update final link

    return ll


def print_result(ll_, n_):
    output = []
    cur_ = ll_
    for i in range(n_):
        output.append(cur_.value)
        cur_ = cur_.nex
    print('Output:', '-'.join(output))


if __name__ == '__main__':
    input_ = input('Input: ')
    ls = input_.split('-')
    ll = parse(ls)

    cur = rearrange(ll, len(ls))
    print_result(ll, len(ls))
