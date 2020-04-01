class Node(object):
    def __init__(self, data=None, children=None):
        self.data = data
        self.children = children

class Solution(object):
    def __init__(self, root=None):
        self.root = root
    @classmethod
    def buid_from(cls, node_list):
        node_dict = {}
        for node_data in node_list:
            #print(node_data)
            data = node_data['data']
            #print(data)
            node_dict[data] = Node(data)
            #print(node_dict[data].children)

        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
                #print(root)
            children = []
            if node_data['children'] != None:
                List = node_data['children']
                #print(List)
                for child in List:
                    #print(child)
                    k = node_dict.get(child)
                    #print(k.data)
                    children.append(k)
            else:
                children = None
            #print(children)
            node.children = children
        return cls(root)
    

    def preorder(self, root):
        if not root:
            return []
        stack,ans = [root],[]

        while stack:
            node = stack.pop()
            ans.append(node)
            if node.children:
                stack.extend(reversed(node.children))
        return ans
    
    def preoder_LastNode1(self,root):
        global node
        if not root:
            return
        stack,ans = [root],[]
        while stack:
            node = stack.pop()
            if node.children:
                stack.extend(reversed(node.children))

        return node

    def lowestCommonAncestor(self,root, u, v):
        if not root:
            return
        stack = [([root],root)]
        res = []
        while stack:
            tmp,node = stack.pop()
            if node.data == u.data or node.data == v.data:
                res.append(tmp)
                if len(res) == 2:
                    break
            if node.children:
                k = len(node.children)
                for i in range(k):
                    if node.children[i]:
                        stack.append((tmp + [node.children[i]], node.children[i]))

        i = 0
        while i < min(len(res[0]), len(res[1])):
            if res[0][i].data != res[1][i].data:
                break
            i += 1
        return res[0][i-1]














node_list = [
    {'data': 'A', 'children': ['B','C','D'], 'is_root': True},
    {'data': 'B', 'children': ['E','F'],     'is_root': False},
    {'data': 'E', 'children': None,          'is_root': False},
    {'data': 'F', 'children': ['J'],         'is_root': False},
    {'data': 'J', 'children': None,          'is_root': False},
    {'data': 'C', 'children': ['G'],         'is_root': False},
    {'data': 'G', 'children': None,          'is_root': False},
    {'data': 'D', 'children': ['H','I'],     'is_root': False},
    {'data': 'H', 'children': None,          'is_root': False},
    {'data': 'I', 'children': None,          'is_root': False},
]

Ntree = Solution.buid_from(node_list)
print(Ntree.root)
List = Ntree.preorder(Ntree.root)

pivotset = []

for u in List:
    print(u.data)
    k = Ntree.preoder_LastNode1(u)
    #print(k.data)
    #if List.index(k) < len(List) - 1:
    if k != List[-1]:
        #v = List[List.index(k) + 1]
        #print(v.data)
        for v in List[List.index(k)+1:]:
            lca = Ntree.lowestCommonAncestor(Ntree.root, u, v)
            pivot = (lca.data, u.data, v.data)
            #pivot = (u.data, v.data)
            pivotset.append(pivot)

print(pivotset)













'''
node_dict = {}
for node_data in node_list:
    #print(node_data)
    data = node_data['data']
    #print(data)
    node_dict[data] = Node(data)
    #print(node_dict[data].children)

for node_data in node_list:
    data = node_data['data']
    node = node_dict[data]
    if node_data['is_root']:
        root = node
    children = []
    if node_data['children'] != None:
        List = node_data['children']
        print(List)
        for child in List:
            #print(child)
            k = node_dict.get(child)
            #print(k.data)
            children.append(k)
    else:
        children = None
    #print(children)
    node.children = children
    if node.children !=None:
        list = node.children
        for i in range(len(list)):
            print(node.children[i].data)
'''

'''

    def buid_from(cls, node_list):
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = Node(data)

        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            children = []
            for child in node_data['children']:
                children.append(node_dict.get(child))
            node.children = children
'''
