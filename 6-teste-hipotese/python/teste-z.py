from statsmodels.stats.proportion import proportions_ztest

# compare 1 mean with a specific value
sample_size = 500
qtt_to_consider = 30
proportion = qtt_to_consider/sample_size

value_to_compare = 0.05

z_stat, p_valor = proportions_ztest(qtt_to_consider, sample_size, value_to_compare, alternative='larger', prop_var=value_to_compare)
print(f'Estatística z: {z_stat:.4f}')
print(f'p-valor: {p_valor:.4f}')

# proportions_ztest(
# qtt to calc the proportion (qtt/N) or array of quantities,
# sample_size or array of sample sizes,
# value_to_compare in Ho, that we want to reach (only for 1 sample),
# alternative: the comparation in Ha: 'two-sided' (default), 'larger', 'smaller',
# prop_var: value of proportion to be used in the variance calculation (p0), only for 1 sample test. 
#   if None (default) it uses the sample proportion (qtt/N)
#   if not None, variance = p0 * (1 - p0) / n, where p0 is the value passed
#)

print("------------------------")
# for 2 samples (test A/B)
sample1_size = 2000
sample1_convertions = 180
sample1_proportion = sample1_convertions/sample1_size

sample2_size = 2200
sample2_convertions = 250
sample2_proportion = sample2_convertions/sample2_size

# doesnt need to pass the proportions, it calcs internally
# [qtt_que_forma_nossa_proporcao1, qtt_que_forma_nossa_proporcao2] , [N1, N2]
z_stat, p_valor = proportions_ztest([sample1_convertions, sample2_convertions], [sample1_size, sample2_size]) # by default is bicaudal

print(f'Estatística z: {z_stat:.4f}')
print(f'p-valor: {p_valor:.4f}')

print("------------------------")
# show that the order doesnt care
z_stat, p_valor = proportions_ztest([sample2_convertions, sample1_convertions], [sample2_size, sample1_size]) # by default is bicaudal

print(f'Estatística z: {z_stat:.4f}')
print(f'p-valor: {p_valor:.4f}')

