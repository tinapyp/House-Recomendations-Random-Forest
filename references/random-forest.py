import numpy as np

class DecisionTree:
    def __init__(self, max_depth=5, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.tree = None

    def fit(self, X, y):
        self.tree = self._build_tree(X, y, depth=0)

    def _build_tree(self, X, y, depth):
        num_samples, num_features = X.shape
        if depth >= self.max_depth or num_samples < self.min_samples_split:
            value = np.mean(y)
            return {'value': value}

        feature_indices = np.random.choice(num_features, int(np.sqrt(num_features)), replace=False)
        best_feature, best_threshold = self._find_best_split(X, y, feature_indices)

        left_indices = np.where(X[:, best_feature] < best_threshold)
        right_indices = np.where(X[:, best_feature] >= best_threshold)

        left_tree = self._build_tree(X[left_indices], y[left_indices], depth + 1)
        right_tree = self._build_tree(X[right_indices], y[right_indices], depth + 1)

        return {'feature_index': best_feature, 'threshold': best_threshold,
                'left': left_tree, 'right': right_tree}

    def _find_best_split(self, X, y, feature_indices):
        best_gain = -float('inf')
        best_feature = None
        best_threshold = None
        for feature_index in feature_indices:
            thresholds = np.unique(X[:, feature_index])
            for threshold in thresholds:
                left_indices = np.where(X[:, feature_index] < threshold)
                right_indices = np.where(X[:, feature_index] >= threshold)
                if len(left_indices[0]) == 0 or len(right_indices[0]) == 0:
                    continue
                gain = self._information_gain(y, y[left_indices], y[right_indices])
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature_index
                    best_threshold = threshold
        return best_feature, best_threshold

    def _information_gain(self, parent, left_child, right_child):
        weight_left = len(left_child) / len(parent)
        weight_right = len(right_child) / len(parent)
        gain = self._gini(parent) - (weight_left * self._gini(left_child) + weight_right * self._gini(right_child))
        return gain

    def _gini(self, y):
        if len(y) == 0:
            return 0
        p = np.bincount(y) / len(y)
        return 1 - np.sum(p ** 2)

    def predict(self, X):
        predictions = []
        for sample in X:
            predictions.append(self._predict_tree(self.tree, sample))
        return np.array(predictions)

    def _predict_tree(self, tree, x):
        if 'value' in tree:
            return tree['value']
        if x[tree['feature_index']] < tree['threshold']:
            return self._predict_tree(tree['left'], x)
        else:
            return self._predict_tree(tree['right'], x)


class RandomForest:
    def __init__(self, n_estimators=100, max_depth=5, min_samples_split=2):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.trees = []

    def fit(self, X, y):
        for _ in range(self.n_estimators):
            tree = DecisionTree(max_depth=self.max_depth, min_samples_split=self.min_samples_split)
            tree.fit(X, y)
            self.trees.append(tree)

    def predict(self, X):
        predictions = []
        for tree in self.trees:
            predictions.append(tree.predict(X))
        predictions = np.mean(predictions, axis=0)
        return predictions

# Example usage
if __name__ == "__main__":
    # Generate some sample data
    np.random.seed(42)
    X = np.random.rand(100, 2)  # Features
    y = np.random.randint(0, 2, 100)  # Labels (0 or 1)

    # Instantiate and fit the random forest
    random_forest = RandomForest(n_estimators=10, max_depth=3)
    random_forest.fit(X, y)

    # Make predictions
    new_data = np.array([[0.1, 0.5], [0.8, 0.2]])
    predictions = random_forest.predict(new_data)
    print("Predictions:", predictions)
