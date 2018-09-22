% load csv dataser
df = csvread('HR_comma_sep.csv')

m = length(df); % number of training examples
fprintf('size: %f, Length %f', size(df), m)
% ignore first row, as thats 0
X = df(2:m, 1);
y = df(2:m, 3);

% plotData(X, y)

X = [ones(m - 1, 1), df(2:m,1)];
theta = zeros(2, 1);
fprintf('%f', theta)
% Some gradient descent settings
num_iters = 1500;
alpha = 0.01;

fprintf('\nTesting the cost function ...\n')
% compute and display initial cost
J = computeCost(X, y, theta);
fprintf('With theta = [0 ; 0]\nCost computed = %f\n', J);

theta = gradientDescent(X, y, theta, alpha, num_iters);

fprintf('Theta found by gradient descent:\n');
fprintf('%f\n', theta);

plot(X(:,2), X*theta, '-')
