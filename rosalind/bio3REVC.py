tran = maketrans("ATCG","TAGC")
print raw_input().translate(tran)[::-1]
