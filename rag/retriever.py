from config import TOP_K, SCORE_THRESHOLD, SEARCH_TYPE

def crear_retriever(vectorstore):

    if SEARCH_TYPE == "similarity_score_threshold":

        retriever = vectorstore.as_retriever(
            search_type=SEARCH_TYPE,
            search_kwargs={
                "k": TOP_K,
                "score_threshold": SCORE_THRESHOLD
            }
        )

    else:

        retriever = vectorstore.as_retriever(
            search_type=SEARCH_TYPE,
            search_kwargs={
                "k": TOP_K
            }
        )

    return retriever