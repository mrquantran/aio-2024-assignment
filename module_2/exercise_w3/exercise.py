import numpy as np


def create_train_data():
    data = [
        ["Sunny", "Hot", "High", "Weak", "no"],
        ["Sunny", "Hot", "High", "Strong", "no"],
        ["Overcast", "Hot", "High", "Weak", "yes"],
        ["Rain", "Mild", "High", "Weak", "yes"],
        ["Rain", "Cool", "Normal", "Weak", "yes"],
        ["Rain", "Cool", "Normal", "Strong", "no"],
        ["Overcast", "Cool", "Normal", "Strong", "yes"],
        ["Overcast", "Mild", "High", "Weak", "no"],
        ["Sunny", "Cool", "Normal", "Weak", "yes"],
        ["Rain", "Mild", "Normal", "Weak", "yes"],
    ]
    return np.array(data)


train_data = create_train_data()
print(train_data)


def compute_prior_probability(train_data):
    y_unique = ["no", "yes"]
    prior_probability = np.zeros(len(y_unique))

    total_samples = len(train_data)
    no_count = np.sum(train_data[:, -1] == "no")
    yes_count = np.sum(train_data[:, -1] == "yes")

    prior_probability[0] = no_count / total_samples
    prior_probability[1] = yes_count / total_samples

    return prior_probability


prior_probability = compute_prior_probability(train_data)
print("P(Play Tennis = No):", prior_probability[0])
print("P(Play Tennis = Yes):", prior_probability[1])

import numpy as np


def compute_conditional_probability(train_data):
    y_unique = ["no", "yes"]
    conditional_probability = []
    list_x_name = []

    for i in range(train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)

        x_conditional_probability = {}
        for y in y_unique:
            y_data = train_data[train_data[:, -1] == y]
            y_count = len(y_data)
            for x in x_unique:
                x_count = np.sum(y_data[:, i] == x)
                x_conditional_probability[(x, y)] = x_count / y_count

        conditional_probability.append(x_conditional_probability)

    return conditional_probability, list_x_name


train_data = create_train_data()
_, list_x_name = compute_conditional_probability(train_data)

print("x1 =", list_x_name[0])
print("x2 =", list_x_name[1])
print("x3 =", list_x_name[2])
print("x4 =", list_x_name[3])


def get_index_from_value(feature_name, list_features):
    return np.where(list_features == feature_name)[0][0]


train_data = create_train_data()
_, list_x_name = compute_conditional_probability(train_data)
outlook = list_x_name[0]
i1 = get_index_from_value("Overcast", outlook)
i2 = get_index_from_value("Rain", outlook)
i3 = get_index_from_value("Sunny", outlook)
print(i1, i2, i3)


def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    x1 = get_index_from_value(X[0], list_x_name[0])
    x2 = get_index_from_value(X[1], list_x_name[1])
    x3 = get_index_from_value(X[2], list_x_name[2])
    x4 = get_index_from_value(X[3], list_x_name[3])

    p0 = prior_probability[0]
    p1 = prior_probability[1]

    p0 *= conditional_probability[0][(X[0], "no")]
    p0 *= conditional_probability[1][(X[1], "no")]
    p0 *= conditional_probability[2][(X[2], "no")]
    p0 *= conditional_probability[3][(X[3], "no")]

    p1 *= conditional_probability[0][(X[0], "yes")]
    p1 *= conditional_probability[1][(X[1], "yes")]
    p1 *= conditional_probability[2][(X[2], "yes")]
    p1 *= conditional_probability[3][(X[3], "yes")]

    if p0 > p1:
        y_pred = 0
    else:
        y_pred = 1

    return y_pred


train_data = create_train_data()
conditional_probability, list_x_name = compute_conditional_probability(train_data)

# Compute P("Outlook" = "Sunny" | Play Tennis = "Yes")
x1 = get_index_from_value("Sunny", list_x_name[0])
print(
    "P('Outlook' = 'Sunny' | Play Tennis = 'Yes') = ",
    np.round(conditional_probability[0][("Sunny", "yes")], 2),
)

train_data = create_train_data()
conditional_probability, list_x_name = compute_conditional_probability(train_data)

# Compute P("Outlook" = "Sunny" | Play Tennis = "No")
x1 = get_index_from_value("Sunny", list_x_name[0])
print(
    "P('Outlook' = 'Sunny' | Play Tennis = 'No') = ",
    np.round(conditional_probability[0][("Sunny", "no")], 2),
)


def train_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probability(train_data)

    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name = compute_conditional_probability(train_data)

    return prior_probability, conditional_probability, list_x_name


X = ["Sunny", "Cool", "High", "Strong"]
data = create_train_data()
prior_probability, conditional_probability, list_x_name = train_naive_bayes(data)
pred = prediction_play_tennis(
    X, list_x_name, prior_probability, conditional_probability
)

if pred:
    print("Ad should go!")
else:
    print("Ad should not go!")
