(ns day-03
  (:require
   [common]))

(defn hit-count [trees right down]
  (let [trees (->> trees (partition 1 down) (map first))
        width (-> trees first count)
        init {:hit-count 0, :pos 0}
        next-line (fn [{:keys [pos] :as acc}
                       tree-line]
                    (let [hit (= \# (get tree-line pos))]
                      (cond-> acc
                        :always (update :pos #(-> % (+ right) (mod width)))
                        hit     (update :hit-count inc))))]
    (:hit-count (reduce next-line init trees))))

(defn -main
  []
  (let [trees (->> (common/input) common/lines)]
    (println (hit-count trees 3 1))
    (println (* (hit-count trees 1 1)
                (hit-count trees 3 1)
                (hit-count trees 5 1)
                (hit-count trees 7 1)
                (hit-count trees 1 2)))))
