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

* inferspin-ur nsname path/to/macro/dir/ path/to/m/prior/samples path/to/f/prior/samples -o path/to/output/dir/

* plothist path/to/post.csv -x chi -o path/to/output/dir/ -b numbins -t _chi

* calcintervals nsname_spin.csv -v -p I,chi -L conflvl -d path/to/post.csv -o path/to/output/dir

###### Infer effective spin for target binary pulsar

* inferchieff-ur nsname path/to/macro/dir/ path/to/m1/prior/samples path/to/m2/prior/samples path/to/f1/prior/samples path/to/f2/prior/samples path/to/costheta1/prior/samples path/to/costheta2/prior/samples -o path/to/output/dir/

* plotcorner path/to/post.csv -x chi1,chi2,chieff -o path/to/output/dir/ -b numbins -t _chieff

* calcintervals nsname_chieff.csv -v -p I,chi,chieff -L conflvl -d path/to/post.csv -o path/to/output/dir

