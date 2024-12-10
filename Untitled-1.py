class MedicalKeywordExtractor:
    def __init__(self, medical_keywords, nlp_model):
        self.medical_keywords = set(medical_keywords)  # Predefined medical vocabulary
        self.nlp_model = nlp_model  # Pretrained NLP model for entity recognition

    def preprocess_text(self, text):
        text = text.lower().strip()
        tokens = self.nlp_model.tokenize(text)
        return tokens

    def extract_keywords(self, text):
        tokens = self.preprocess_text(text)
        identified_keywords = []

        for token in tokens:
            if token in self.medical_keywords:  # Match against predefined vocabulary
                identified_keywords.append(token)
            else:
                entities = self.nlp_model.identify_entities(token)  # Identify named entities
                identified_keywords.extend([e for e in entities if e in self.medical_keywords])

        return list(set(identified_keywords))  # Return unique keywords
    





class MedicalTermInterpreter:
    def __init__(self, ai_model_api, search_engine_api):
        self.ai_model_api = ai_model_api
        self.search_engine_api = search_engine_api

    def query_ai_model(self, term):

        response = self.ai_model_api.call({
            "input": f"Explain the medical term '{term}' in simple language.",
            "temperature": 0.7
        })
        return response.get("explanation", "No explanation available.")

    def interpret_term(self, term, use_model=True):

        if use_model:
            return self.query_ai_model(term)
        


