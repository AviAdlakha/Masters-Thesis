%code to concatenate data

clear all
clc
% Load the first *.mat file (matlab1.mat)
x = load ('Firing rates 0.2.mat');
y = load ('Firing rates 0.4.mat');
C = load ('Firing rates 0.6.mat');
D = load ('Firing rates 0.8.mat');
E = load ('Firing rates 1.mat');
F = load ('Firing rates 1.2.mat');
G = load ('Firing rates 1.4.mat');
H = load ('Firing rates 1.6.mat');
I = load ('Firing rates 2.mat');
J = load ('Firing rates 2.6.mat');
K = load ('Firing rates 3.mat');
  
vrs = fieldnames(x);
if ~isequal(vrs,fieldnames(y))
    error('Different variables in these MAT-files')
end
% Concatenate data
for k = 1:length(vrs)
    x.(vrs{k}) = [x.(vrs{k});y.(vrs{k});C.(vrs{k});D.(vrs{k});E.(vrs{k});F.(vrs{k});G.(vrs{k});H.(vrs{k});I.(vrs{k});J.(vrs{k});K.(vrs{k})];
    
end

x.(vrs{2}) = reshape(x.(vrs{2}),25,[])
x.(vrs{3}) = reshape(x.(vrs{3}),25,[])
x.(vrs{1}) = reshape(x.(vrs{1}),100,[])

save('Combined','-struct','x')
