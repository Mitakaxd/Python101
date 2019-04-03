# # reducing string
# def reduce_file_path(path):
#     lst=path.split('/')
#     newlst=[]
#     for index in range(len(lst)-1):
#         if lst[index]!="." and lst[index]!="/." and lst[index+1]!=".." and lst[index+1]!="/..":
#             newlst.append(lst[index])
#     if ".." or "/.." in lst:
#         return reduce_file_path("/".join(newlst))
#     return "/".join(newlst)




def reduce_file_path(path):
    lst=path.split('/')
    endpath=[]
    for dir_path in lst:
        if dir_path=='.':
            continue
        elif dir_path=='..':
            endpath.pop()
        else:
            endpath.append(dir_path)
    return '/'.join(endpath)

print(reduce_file_path("/srv/../"))
print(reduce_file_path("/srv/www/htdocs/wtf/"))
