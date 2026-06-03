---
layout: splash
title: Ontario Cryptography Day

feature_row:
  - title: "Friday, June 5, 2026"
    excerpt: "9:40am–4:30pm"
  - title: "McMaster University"
    excerpt: "CIBC Hall"
  - title: "Registration"
    # excerpt: "Registration is free but required"
    excerpt: "Registration is now closed"
    # url: "https://docs.google.com/forms/d/e/1FAIpQLSfpuqHctOoWZmVcKbfWdq9hqAJmKGUw0B-2C8beyodTRw4wLw/viewform?usp=dialog"
    # btn_label: "Register now"
    # btn_class: "btn btn--success"
header:
  overlay_image: /images/campus-mcmaster.jpg
  overlay_filter: "rgba(0, 40, 70, 0.45)"
excerpt: "Friday, June 5, 2026 • McMaster University"

---


**Ontario Cryptography Day** aims to bring together the cryptography community in Ontario for a day of research talks and discussions. We hope to establish a recurring event rotating through universities in Ontario, Canada.

The event is open to academic, industry, and public sector researchers and practitioners in cryptography, but registration is required.

{% include feature_row %}

<div class="program-block">
<h2>Program</h2>
<table class="program-table">
<tr>
  <td>09:40–10:00</td>
  <td></td>
  <td>Registration</td>
</tr>
  
<tr>
  <td>10:00–10:45</td>
  <td></td>
  <td><b><a target="_blank" href="https://sam-jaques.appspot.com/">Sam Jaques</a></b>, University of Waterloo.<br>
  <i>Sharing Seriously Short Shamir Secrets Safely</i>
  <details>
  <summary>Abstract</summary>
While computers easily handle cryptographic key material all the time, real people (even experts) are notoriously bad at this. Threshold cryptography promises to help, by sharing cryptographic keys among multiple people and/or devices. Even if you drop your phone in the ocean or your laptop gets hacked, your keys should remain both safe and available for signing, decryption, or whatever else you need. A particular problem here is distributed generation of the secret key, such that no participant knows the full key at any time. Good techniques exist for discrete log keys, which are uniformly random, but keys for lattice-based schemes must be short. In this talk I will explain the nuances of this problem, previous approaches, and our solution: the structure of zero-knowledge proofs, multi-party computation, and lattices turn out to work together extremely well, allowing us to generate secret vectors smaller than any other scheme permits. This is joint work with Chelsea Komlo and Yijie Zhao.
  </details>
  </td>
</tr>

<tr>
  <td>10:45–11:15</td>
  <td></td>
  <td>Coffee break</td>
</tr>

<tr>
  <td>11:15–12:15</td>
  <td></td>
  <td>Invited keynote: <b><a target="_blank" href="https://freedom.press/people/rowen-s/">Rowen Shane</a></b>, Freedom of the Press Foundation.<br>
  <i>SecureDrop Protocol: Lessons Learned From a Decade of Deployment</i>
  <details>
  <summary>Abstract</summary>
    Confidential sources are vital for investigative journalism, but the digital age makes it difficult for would-be sources to remain anonymous.  How are privacy-preserving communications tools used in a whistleblowing context, and what challenges do these tools face during the transition to quantum-safe encryption? <br><br>
This talk presents SecureDrop Protocol, a redesigned version of Freedom of the Press Foundation’s open-source whistleblowing platform SecureDrop that seeks to improve on both the security model and deployability of the system’s existing design. We discuss the redesign’s motivations and constraints, some of which preclude the use of existing protocols such as Signal and MLS, and present the most recent core library specification, designed in collaboration with ETH Zurich, formally modelled using Tamarin, and analyzed using a combination of formal and game-based proofs. We also touch on: ongoing pre-deployment research topics; IETF standards; cryptographic hot potatoes; the challenge and ethics of requirements-gathering with at-risk users; and what happens when your model explodes the Tamarin prover. A portion of this talk was recently presented at RWC2026.
  </details>
  </td>
</tr>

<tr>
  <td>12:15–13:45</td>
  <td></td>
  <td>Lunch</td>
</tr>

<tr>
  <td>13:45–14:30</td>
  <td></td>
  <td><b><a target="_blank" href="https://www.leonardocolo.com/">Leonardo Colò</a></b>, University of Waterloo.<br>
  <i>Zero-Knowledge Proofs of Isogeny Diamonds</i>
  <details>
  <summary>Abstract</summary>
  Commutative diagrams of isogenies between supersingular elliptic curves, which we call isogeny diamonds, have become fundamental to isogeny-based cryptography for both constructive and cryptanalytic purposes. In parallel, proofs of knowledge of isogenies have been widely studied and have found many applications. In this work, we combine these two directions and introduce zero-knowledge proofs of isogeny diamonds, namely, proofs of knowledge of isogenies together with the fact that they form a commutative diagram. We present three constructions in two settings. The first, which we call the Windmill-ZKP, assumes that the prover knows only two parallel isogenies in the diamond which is relevant for multi-party computation of M-SIDH. The other two, Cube-ZKP and Kani-ZKP, assume that the prover knows all four isogenies.   
  </details>
  </td>
</tr>

<tr>
  <td>14:30–15:15</td>
  <td></td>
  <td><b><a target="_blank" href="https://profiles.laps.yorku.ca/profiles/lxue03/">Liang Xue</a></b>, York University.<br>
  <i>Robust and Trustworthy Harmful Media Detection in End-to-End Encrypted Communication</i>
  <details>
  <summary>Abstract</summary>
  Private Hash Matching (PHM) enables harmful media detection in End-to-End Encrypted (E2EE) communication by comparing user media hashes with a server-side set of known harmful hashes, without exposing the server’s hash set or revealing unmatched user media. However, existing PHM schemes often fail to detect slightly modified media, lack efficient dynamic updates, and provide limited verifiability, which weakens transparency and public trust. In this talk, I will present VeriFPHM, a verifiable fuzzy PHM scheme for robust and trustworthy harmful content moderation. VeriFPHM uses multivariate polynomial commitments and adaptive Merkle trees to support batch verification of hash-set integrity and consistency. To enable efficient updates, it maps index-tree subtrees to Cuckoo hash buckets, allowing partial-tree updates instead of full reconstruction. To prevent over-censorship and maintain detection efficiency, we design a two-step fuzzy matching protocol. Specifically, coarse-grained matching filters out benign media using enhanced index trees with efficient bucket access, followed by distance-aware fine-grained matching using a lightweight Learning with Parity Noise (LPN)-based Vector Oblivious Linear Evaluation (VOLE) protocol. Security analysis confirms that VeriFPHM preserves the privacy of both user content and the server-side hash set. Experiments demonstrate up to 100x faster certification and significantly improved update performance, while maintaining high detection accuracy compared with state-of-the-art schemes.
  </details>
  </td>
</tr>

<tr>
  <td>15:15–15:45</td>
  <td></td>
  <td>Coffee break</td>
</tr>

<tr>
  <td>15:45–16:30</td>
  <td></td>
  <td><b><a target="_blank" href="https://www.cs.toronto.edu/~ziyang/">Ziyang Jin</a></b>, University of Toronto.<br>
  <i>Non-Interactive Secure Computation with Constant Communication Overhead</i>
  <details>
  <summary>Abstract</summary>
    We study the communication complexity of non-interactive secure computation (NISC) protocols with security against malicious adversaries. We give a general NISC protocol for any two-party function computed by a Boolean circuit C using only O(|C|λ) bits of communication, where λ is an exact security parameter. This protocol is unconditionally secure in the random oracle model, assuming a standard random OT correlations setup. Compared to Yao's semi-honest protocol, our protocol incurs only a constant communication overhead and achieves security against malicious parties with no additional interaction. Prior works achieved such constant overhead by either using a larger number of rounds or more structured correlations.
  </details>
  </td>
</tr>

</table>
</div>


## Travel

**CIBC Hall:** located on the 3rd floor of the [MUSC building](https://maps.app.goo.gl/xTKXRptUnh9qmZuy6). The closest parking lots to MUSC are [Parking Lot B](https://maps.app.goo.gl/BkXQ1WQa5L6gVDMi7) and [Parking Lot C](https://maps.app.goo.gl/Wctnk71uameHcT5S8).

**Public transport:** The McMaster bus terminal, located between Mary E. Keyes Residence and H. G. Thode Library, is used exclusively by [GO Transit](https://www.gotransit.com/en/student-savings/go-to-school). [Hamilton Street Railway (HSR)](https://www.hamilton.ca/home-neighbourhood/hsr) provides connecting routes with nearby stops. Additional services, including [FlixBus](https://www.flixbus.ca/), as well as dedicated McMaster shuttle buses, are also available.


## Map

<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1452.7123666177122!2d-79.91901554317556!3d43.263476945962566!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x882c9b53630b56ef%3A0xf87279542227b6b2!2sMcMaster%20University%20Student%20Centre!5e0!3m2!1sen!2sca!4v1777737383300!5m2!1sen!2sca" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>


## Organizers

- [Jake Doliskani](https://www.eng.mcmaster.ca/cas/faculty/jake-doliskani/), McMaster University
- [Armin Ahmadkhaniha](https://arminahmadkhaniha.github.io/), McMaster University
- **Lu Chen**, McMaster University

For more information, please email [jake.doliskani@mcmaster.ca](mailto:jake.doliskani@mcmaster.ca). 


## Past events

- [November 28, 2025 • Fields Institute, Toronto](/2025-11-28.html)
- [June 6, 2025 • University of Waterloo](/2025-06-06.html)
