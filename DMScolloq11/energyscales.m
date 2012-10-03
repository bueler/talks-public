% ENERGYSCALES compute scales associated to 1 m^3 of ice, and define 1 Echelmeyer

m = 910.0;
secpera = 31556926.0;

fprintf('energies in Joules:\n')
v = 1000.0 / secpera;
Ekinetic = 0.5 * m * v^2

g = 9.81;
h = 1000.0;
Epotential = m * g * h   % = 1 Echelmeyer of energy

C = 2009.0;
dT = 10.0;
Esensible = m * C * dT

L = 3.34e5;
Elatent = m * L

fprintf('\nenergies in Echelmeyers:\n')

echel = Epotential;
Ekinetic = Ekinetic / echel
Epotential = Epotential / echel
Esensible = Esensible / echel
Elatent = Elatent / echel

