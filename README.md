# ns-ur-inf
Code for inference of neutron star properties with universal relations.

---

### Scripts

###### Generate prior samples from specified distributions

* makepriorsamples varname distr param1,param2,... -v -n numsamps -o path/to/output/dir/

###### Extrapolate binary neutron star spins to merger

* getspinatmerger spin Tc tau -v

###### Infer moment of inertia and spin, plus effective spin for a binary

* inferspin-ur nsname path/to/Lambda14/prior/samples.csv path/to/m/prior/samples.csv path/to/f/prior/samples.csv -v -n nummcsamps -o path/to/output/dir/

* inferchieff-ur nsname path/to/Lambda14/prior/samples.csv path/to/m1/prior/samples.csv path/to/m2/prior/samples.csv path/to/f1/prior/samples.csv path/to/f2/prior/samples.csv path/to/costheta1/prior/samples.csv path/to/costheta2/prior/samples.csv -v -n nummcsamps -o path/to/output/dir/

###### Infer tidal deformability, radius and compactness

* inferradius-ur nsname path/to/Lambda14/prior/samples.csv path/to/m/prior/samples.csv -v -n nummcsamps -o path/to/output/dir/

###### Calculate confidence intervals

* calcintervals postsamps.csv -v -p I,chi -L conflvl -d path/to/post/samples/dir/ -o path/to/output/dir/

---

### Tools

###### Make histogram of single observable

* plothist priorsamps.csv,postsamps.csv -x var -l xmin,xmax -d path/to/samples/dir/ -o path/to/output/dir/

###### Make corner plot of several observables

* plotcorner priorsamps.csv,postsamps.csv -x var1,var2,... -l x1min,x1max,x2min,x2max,... -d path/to/samples/dir/ -o path/to/output/dir/

---

### Instructions for performing inference

###### Generate priors on observables

* makepriorsamples varname distr param1,param2,... -v -n numsamps -o path/to/output/dir/

###### Infer spin for target pulsar

* inferspin-ur nsname path/to/Lambda14/prior/samples path/to/m/prior/samples path/to/f/prior/samples -o path/to/output/dir/

* plotcorner path/to/prior.csv,path/to/post.csv -x I,chi -o path/to/output/dir/ -b 40 -t _chi -q 0.05,0.5,0.95 -F 3 -A '$I$','$\chi$' -C 0.5,0.9

* calcintervals nsname_spin.csv -v -p I,chi -L conflvl -d path/to/post.csv -o path/to/output/dir

###### Infer effective spin for target binary pulsar

* inferchieff-ur nsname path/to/Lambda14/prior/samples path/to/m1/prior/samples path/to/m2/prior/samples path/to/f1/prior/samples path/to/f2/prior/samples path/to/costheta1/prior/samples path/to/costheta2/prior/samples -o path/to/output/dir/

* plotcorner path/to/prior.csv,path/to/post.csv -x I1,chi1,chieff -o path/to/output/dir/ -b 40 -t _chieff -q 0.05,0.5,0.95 -F 7 -A '$I_1$','$\chi_1$','$\chi_{\rm eff}$' -C 0.5,0.9 -f corner

* calcintervals nsname_chieff.csv -v -p I1,I2,chi1,chi2,chieff -L 0.9 -d path/to/post.csv -o path/to/output/dir

