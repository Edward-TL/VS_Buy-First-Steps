
# nltk.download('punkt')
# nltk.download('stopwords')
# stopwords = set(stopwords.words('spanish'))

def create_corpus_points(user_request, page_names, header):
    corpus = {}
#     pattern = r'''(?x)                  # Flag para iniciar el modo verbose
#               (?:[A-Z]\.)+            # Hace match con abreviaciones como U.S.A.
#               | \w+(?:-\w+)*         # Hace match con palabras que pueden tener un guión interno
#               | \$?\d+(?:\.\d+)?%?  # Hace match con dinero o porcentajes como $15.5 o 100%
#               | \.\.\.              # Hace match con puntos suspensivos
#               | [][.,;"'?():-_`]    # Hace match con signos de puntuación
# '''
    for names_array in page_names:
        points = len(names_array)
        for product in names_array:
            if product != None:
                # words = nltk.regexp_tokenize(product, pattern)
                product = product.lower()
                words = product.split()
                
                for word in words:
                    word = word.lower()
                    if word in corpus:
                        last_points = corpus[word]
                        total_points = last_points + points
                        corpus[word] = total_points
                    else:
                        corpus[word] = points
                points -= 1

    return corpus
    
#Is use page by page. Not for all the request.
def hit_points_info(user_request, products_dict, corpus, array=True, dictionary=False):
#     pattern = r'''(?x)                  # Flag para iniciar el modo verbose
#               (?:[A-Z]\.)+            # Hace match con abreviaciones como U.S.A.
#               | \w+(?:-\w+)*         # Hace match con palabras que pueden tener un guión interno
#               | \$?\d+(?:\.\d+)?%?  # Hace match con dinero o porcentajes como $15.5 o 100%
#               | \.\.\.              # Hace match con puntos suspensivos
#               | [][.,;"'?():-_`]    # Hace match con signos de puntuación
# '''
    minus_words = ('cambio', 'descompuesta')
    if dictionary == True:
        hits_dict = {}
    if array == True:
        hits_array = []

    user_request = user_request.lower()
    request_set = set(user_request.split())
    request_len = len(request_set)

    if len(products_dict['names']) > 0 and products_dict['names'] != None:
        for product_name in products_dict['names']:
            if product_name != None:
                # product_name_words = nltk.regexp_tokenize(product_name, pattern)
                product_name = product_name.lower()
                product_name_words = product_name.split()

                # Give points by the position and frequency of every word in all the
                # products given by the the four pages. Highest, frequency, highest relevance
                total_points = 0
                for word in product_name_words:
                    if word in minus_words:
                        total_points = total_points - 1000
                    else:
                        if word in corpus:
                            word_points = corpus[word]
                            total_points = total_points + word_points
                        else:
                            pass

                # Verifies that every word of the request is in the product name
                # If there's none, even with the highest score it would be turn in 0
                product_name_set = set(product_name_words)
                request_points = 0
                for word in request_set:
                    if word in product_name_set:
                        request_points = request_points + 1
                
                coverage_of_request = request_points / request_len

                final_points = int(total_points*coverage_of_request)

            else: #of if product_name != None:
                final_points = 0
                
            if dictionary == True:
                hits_dict[product_name] = final_points
            if array == True:
                hits_array.append(final_points)

    # For testing of the fucntion
    if dictionary == True and array == False:
        return hits_dict
    elif array == True and dictionary == False:
        return hits_array
    else:
        return hits_dict, hits_array
