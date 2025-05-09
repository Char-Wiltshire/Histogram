library(ggplot2)

regions <- c(
  'NCR', 'Cordillera', 'Region 1', 'Region 2', 'Region 3', 'Region 4A', 'MIMAROPA',
  'Region 5', 'Region 6', 'Region 7', 'Region 8', 'Region 9', 'Region 10',
  'Region 11', 'Region 12', 'Caraga', 'ARMM'
)

of <- c(9.2, 11.0, 11.8, 16.1, 8.8, 7.6, 5.9, 4.6, 13.2, 6.0, 6.3, 7.1, 6.5, 7.3, 12.4, 5.9, 6.9)
ofw <- c(17.3, 16.0, 18.0, 21.9, 7.2, 13.3, 6.6, 8.5, 14.2, 10.2, 8.3, 9.9, 10.5, 11.0, 9.4, 5.4, 23.8)
emigrants <- c(1.2, 2.9, 2.4, 1.5, 0.8, 3.5, 0.9, 0.3, 0.9, 1.0, 0.3, 0.3, 0.4, 0.3, 2.2, 2.0, 1.6)

data <- data.frame(
  Region = rep(regions, times = 3),
  Category = factor(rep(c("With OF", "With OFW", "With Emigrants"), each = length(regions))),
  Percentage = c(of, ofw, emigrants)
)

ggplot(data, aes(x = Percentage, y = Region, fill = Category)) +
  geom_bar(stat = "identity", position = position_dodge()) +
  geom_text(aes(label = paste0(Percentage, "%")),
            position = position_dodge(width = 0.9),
            hjust = -0.1, size = 2.5) +
  labs(title = "2018 National Migration Survey by Region",
       x = "Percentage", y = "Region") +
  theme_minimal() +
  theme(legend.title = element_blank()) +
  xlim(0, max(data$Percentage) + 5)