def solve(preorder, inorder):

    if not preorder:
        return

    root = preorder[0]
    idx = inorder.index(root)
    solve(preorder[1:idx+1], inorder[0:idx])
    solve(preorder[idx+1:], inorder[idx+1:])
    print(root, end=" ")


for _ in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    solve(preorder, inorder)
    print()
