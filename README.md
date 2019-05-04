# techolution
> Utility for checking image duplicates

### Fundamental approach: Concept-based image indexing
> Using imageUrl to identify duplicates.
- Here I have used the imageUrlStr of the product as a basis to identify if the product is a duplicate or not.
- Algorithm: Hashing
- Time complexity for finding duplicates in N images: O(N) (Disregarding hashing overhead)

This is the most basic approach. Any product which has the same image will necessarily be a duplicate.
I have used hashing so that the algorithm works in O(N) complexity.


### Content based image similarity approach: Scale-Invariant Feature Transform (SIFT)
> Using the similarity of images(content) to say if the product is duplicate or not
- I have created a module called image_util which has functions to check content similarity.
- Algoritm: Scale-Invariant Feature Transform

### Other possible approaches:
> I was not able to try these due to lack of time
- CNN driven Content-based Image Retrieval (CBIR) using Auto Encoders
- Hamming Distance and DHask driven similarity check.



