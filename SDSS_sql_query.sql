SELECT top 100
  --- basic info
  G.objID,
  GSI.specObjID,
  G.ra, 
  G.dec, 
  --- basic spectral data
  S.z, 
  S.zErr, 
  S.velDisp, 
  S.velDispErr,
  --- some useful imaging parameters
  G.modelMag_u, 
  modelMagErr_u, 
  G.modelMag_g, 
  modelMagErr_g,
  G.modelMag_r, 
  modelMagErr_r, 
  G.modelMag_i, 
  modelMagErr_i,
  G.modelMag_z, 
  modelMagErr_z, 
  G.petroR50_r, 
  G.petroR90_r,
  --- line fluxes for BPT diagram and other derived spec. parameters
  GSL.nii_6584_flux, 
  GSL.nii_6584_flux_err, 
  GSL.h_alpha_flux,
  GSL.h_alpha_flux_err, 
  GSL.oiii_5007_flux, 
  GSL.oiii_5007_flux_err,
  GSL.h_beta_flux, 
  GSL.h_beta_flux_err, 
  GSL.h_delta_flux,
  GSL.h_delta_flux_err, 
  GSX.d4000, 
  GSX.d4000_err, 
  GSE.bptclass,
  GSE.oh_p2p5,
  GSE.oh_p16,
  GSE.oh_p50,
  GSE.oh_p84,
  GSE.oh_p97p5,
  GSE.lgm_tot_p50, 
  GSE.sfr_tot_p50
INTO mydb.SDSSspecgalsDR14 
FROM SpecObj as S
  JOIN Galaxy as G
  ON G.ObjID = S.bestObjID
  JOIN GalSpecLine as GSL
  ON GSL.specObjID = S.specObjID
  JOIN GalSpecInfo AS GSI
  ON GSI.specObjID = S.specObjID
  JOIN GalSpecIndx AS GSX
  ON GSX.specObjID = S.specObjID  
  JOIN GalSpecExtra AS GSE
  ON GSE.specObjID = S.specObjID
  --- add some quality cuts to get rid of obviously bad measurements
WHERE (G.petroMag_r > 10 AND G.petroMag_r < 18)
  AND (G.modelMag_u-G.modelMag_r) > 0
  AND (G.modelMag_u-G.modelMag_r) < 6
  AND (modelMag_u > 10 AND modelMag_u < 25)
  AND (modelMag_g > 10 AND modelMag_g < 25)
  AND (modelMag_r > 10 AND modelMag_r < 25)
  AND (modelMag_i > 10 AND modelMag_i < 25)
  AND (modelMag_z > 10 AND modelMag_z < 25)
  AND S.rChi2 < 2
  AND (S.zErr > 0 AND S.zErr < 0.01)
  --- trim the sample
  AND S.z > 0.02
  AND GSE.oh_p50 != -9999
