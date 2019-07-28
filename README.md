# ns-ur-inf
Code for inference of neutron star properties with universal relations.

---

### Scripts

##### GET-BINSPINFREQS

* GET-BINSPINFREQS nsname path/to/postsamps.csv "priorcol1,priorcol2" numsamps conflvl /path/to/output

Infer moment of inertia and spin frequency from correlated mass and dimensionless spin distributions (given as discrete posterior samples) for a binary, plus GW170817 Lambda_1.4 bounds; report symmetric 90% confidence interval and median.

##### GET-SPINFREQ

* GET-SPINFREQ nsname path/to/postsamps.csv "priorcol1,priorcol2" numsamps conflvl /path/to/output

Infer moment of inertia and spin frequency from mass and dimensionless spin distributions (given as discrete posterior samples), plus GW170817 Lambda_1.4 bounds; report symmetric 90% confidence interval and median.

##### GET-ANGMOM

* GET-ANGMOM nsname "m_med,m_std,m_ub" "omega_med,omega_std" numsamps conflvl /path/to/output

Infer moment of inertia and dimensionless spin from mass and rotational frequency distributions (given as Gaussians), plus GW170817 Lambda_1.4 bounds; report symmetric 90% confidence interval and median.

##### GET-NONROTPROPS

* GET-NONROTPROPS nsname "m_med,m_std,m_ub" numsamps conflvl /path/to/output

Infer radius, compactness, moment of inertia and tidal deformability from mass distributions (given as Gaussian), plus GW170817 Lambda_1.4 bounds; report symmetric 90% confidence interval and median.

##### inferprops

* inferprops nsname -p prop1,prop2 -n numsamps -D priordistr1,priordistr2 -P prior1param1+prior1param2,prior2param1 -o /path/to/output

Infer posterior distributions on specified properties based on input priors and universal relations.

##### calcintervals

* calcintervals props.csv -p prop -L conflvl -d /path/to/props -o /path/to/output -t _tag

Calculate median and symmetric confidence interval for specified property.

##### plothist

* plothist props.csv -x f -t f -b 100 -d /path/to/props -o path/to/output -f spinfreq -A "\$f\$ [Hz]","" -O lb+ub,med,44.+59.,707.+716. -s 0+"--"+"sym90CL (lb;ub)",0+"-"+"median (med)",4+"-"+"max_DNS",3+"-"+"max_PSR"

Plot spin frequency posterior histogram with median, confidence interval and reference curves from observations of pulsars.

##### plotcorner

* plotcorner prior_props.csv,props.csv -x f1,f2 -d /path/to/props -o path/to/output -f spinfreqs -C 0.5,0.9 -l 0.,1000.,0.,1000. -A '$f_1$ [Hz]','$f_2$ [Hz]' -q 0.9 -T 716.,59.

Make corner plot of component spin frequencies for a binary system with confidence regions, upper bounds and reference curves from observations of pulsars.
