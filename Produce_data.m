%to produce data matrix

clc
A = load('Combined new WT Cineole 04.mat','FM')
B = load('Combined new WT Euginol 04.mat','FM')
C = [A;B]
D = cell2mat(struct2cell(C))
D = D'
writematrix(D,'Data WT 04.csv')