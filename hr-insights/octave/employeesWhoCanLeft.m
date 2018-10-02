df = csvread('HR_comma_sep.csv');

m = length(df); 

idx = (df(2:m, 7)==1 & df(2:m, 9) == 'technical');
A_exists = df(idx,:)

idx = (df(2:m, 7)==0);
A_left = df(idx,:)

m = length(A_exists); % number of training examples
fprintf('size: %f, Length %f', size(A_exists), m)
% ignore first row, as thats 0
X = A_exists(2:m, 1);
y = A_exists(2:m, 2);

%plotData(X, y, 'Satisfaction Level', 'Employess will left or not?', 'Employees ratention v/s satisfaction rate')

plot(X, y, 'r.', 'MarkerSize', 10)

hold on;

m = length(A_left); % number of training examples
fprintf('size: %f, Length %f', size(A_left), m)
% ignore first row, as thats 0
X = A_left(2:m, 1);
y = A_left(2:m, 2);

plot(X, y, 'y.', 'MarkerSize', 10)