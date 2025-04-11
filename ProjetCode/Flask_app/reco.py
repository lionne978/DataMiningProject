def recommend_products(rules, user_basket, top_n=5):
    recommendations = []
    for _, row in rules.iterrows():
        if row['antecedents'].issubset(user_basket) and not row['consequents'].issubset(user_basket):
            recommendations.append((row['consequents'], row['confidence'], row['lift']))

    recommendations = sorted(recommendations, key=lambda x: (x[1], x[2]), reverse=True)

    final_reco = []
    seen = set()
    for items, _, _ in recommendations:
        for item in items:
            if item not in seen:
                final_reco.append(item)
                seen.add(item)
            if len(final_reco) >= top_n:
                break
        if len(final_reco) >= top_n:
            break

    return final_reco
