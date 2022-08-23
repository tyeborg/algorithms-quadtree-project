# Algorithms: QuadTree Project

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/tyeborg/algorithms-quadtree-project)
![GitHub top language](https://img.shields.io/github/languages/top/tyeborg/algorithms-quadtree-project)
![GitHub last commit](https://img.shields.io/github/last-commit/tyeborg/algorithms-quadtree-project)

The objective of this project is to code a QuadTree (level n > 1) based on the *long_wgs*, *lat_wgs* location from each row from the retailer's file. Each leaf of the Quadtree holds a list where each element is a `TupleT`: (`long_wgs`, `lat_wgs`, `retailer`, `postcode`).

* **Input**: A pair *Longitude*, *Latitude*.
* **Output**: An ST structure that corresponds to the retailer located on the *Latitude*, *Longitude* provided.

**Procedure:**
1. Ask the user for a `longitude` and a `latitude` from the retailer's file (uk_glx_open_retail_points_v20_202104.csv).
2. Once you located the correct leaf, search on the list for the correct `TupleT`.
3. Use the retailer/postcode located in `TupleT` to search for `ST` on the hash table.

For example, if the input is -4.452243148 (longitude), 54.16746806 (latitude), the output should be:

```bash
Please enter longitude: -4.452243148
'-4.452243148' has been accepted...

Please enter latitude: 54.16746806
'54.16746806' has been accepted...

--------Location Information--------
Store name: Spar - Onchan
Address: 14 Port Jack nan
Town: Isle of Man
Postcode: IM3 1EB
Size Band: < 3,013 ft2 (280m2)
------------------------------------
```

## Languages & Tools Utilized

<p float="left">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,vscode" />
  </a>
</p>
