# ns-ur-inf
Code for inference of neutron star properties with universal relations.

---

### Scripts

##### DO-SPIN

* DO-SPIN nsname nsmass nsmass_std omega omega_std nsamps conflvl /path/to/output

Infer dimensionless spin and moment of inertia from Gaussian mass and rotational frequency distributions, plus GW170817 Lambda_1.4 bounds; report symmetric 90% confidence interval and median.

##### DO-NS

* DO-NS nsname nsmass nsmass_std lambda1.4_betap lambda1.4_betaq omega omega_std nsamps conflvl /path/to/output

Infer radius, compactness, tidal deformability, dimensionless spin and moment of inertia from Gaussian mass and rotational frequency distributions, plus GW170817 Lambda_1.4 bounds; report symmetric 90% confidence interval and median.
