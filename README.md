# ns-ur-inf
Code for inference of neutron star properties with universal relations.

---

### Scripts

##### GET-SPINFREQ

* GET-SPINFREQ nsname path/to/postsamps.csv "priorcol1,priorcol2" numsamps conflvl /path/to/output

Infer moment of inertia and spin frequency from mass and dimensionless spin distributions (given as discrete posterior samples), plus GW170817 Lambda_1.4 bounds; report symmetric 90% confidence interval and median.
