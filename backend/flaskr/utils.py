class helper():
    def paganation(sefl, request, data):
        page = request.args.get('page', 1, type=int)
        size = request.args.get('size', 10, type=int)
        startIndex = (page - 1) * size
        endIndex = startIndex + size
        return data[startIndex:endIndex]
